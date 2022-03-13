const URL = "http://localhost:5000"

const generate = async (url) => {
  let base_url = `${URL}/generate`;

  const headers = new Headers({
    "Content-Type": "application/json"
})

  const res = await fetch(base_url, {
    method: "post",
    headers:headers,
    body: JSON.stringify({
      "url": url
    })
  })

  data = await res.json()
  
  document.querySelector("#url-placeholder").textContent = `http://localhost:5000/r/${data.token}`
}

document.querySelector("#form").addEventListener("submit", (event) => {
  event.preventDefault();
  let data = new FormData(document.querySelector("#form"))

  generate(data.get("url"))
})