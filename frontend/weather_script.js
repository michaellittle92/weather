async function create_weather_element(element) {
  let weather_element = document.createElement("div");

  let image = document.createElement("img");
  image.src = element["icon"];

  let day = document.createElement("label");
  let max_temp = document.createElement("label");
  let min_temp = document.createElement("label");

  let day_content = document.createTextNode(element["day"]);
  let max_temp_content = document.createTextNode(element["max_temp"] + "° / ");
  let min_temp_content = document.createTextNode(element["min_temp"] + "°");

  day.appendChild(day_content);
  max_temp.appendChild(max_temp_content);
  min_temp.appendChild(min_temp_content);

  weather_element.appendChild(image);
  weather_element.appendChild(day);
  weather_element.appendChild(max_temp);
  weather_element.appendChild(min_temp);

  container.appendChild(weather_element);

  weather_element.classList.add("weather_element");
  image.classList.add("icon");
  day.classList.add("day");
  max_temp.classList.add("max_temp");
  min_temp.classList.add("min_temp");
}

async function getData() {
  const url = "http://127.0.0.1:8000/weather_data";

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`response status: ${response.status}`);
    }
    const json = await response.json();
    console.log(json);
    const loading_message = document.getElementById("loading");
    loading_message.remove();
    for (let i = 0; i < json.length; i++) {
      create_weather_element(json[i]);
    }
  } catch (error) {
    console.error(error.message);
  }
}

async function main() {
  let container = document.getElementById("container");
  getData();
}

main();
