const express = require("express");

const app = express()

app.get("/", (req, res) => {
    res.send("hello!")
})

app.listen(8080, () => {
    console.log("Listening on http://localhost:8080/")
})