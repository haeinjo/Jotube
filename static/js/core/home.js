"use strict"

const uploadBtn = document.querySelector(".right__upload");
const uploadDes = document.querySelector(".jtHeader__uploadDes");
const appBtn = document.querySelector(".right__app");
const appDes = document.querySelector(".jtHeader__appDes");
const notiBtn = document.querySelector(".right__noti");
const notiDes = document.querySelector(".jtHeader__notiDes");


// Hover upload button
uploadBtn.addEventListener("mouseenter", (e) => {
    uploadDes.classList.toggle("hidden_element");
})
uploadBtn.addEventListener("mouseleave", (e) => {
    uploadDes.classList.toggle("hidden_element");
})

// Hover app button
appBtn.addEventListener("mouseenter", () => {
    appDes.classList.toggle("hidden_element");
})
appBtn.addEventListener("mouseleave", () => {
    appDes.classList.toggle("hidden_element");
})

// Hover noti button
notiBtn.addEventListener("mouseenter", () => {
    notiDes.classList.toggle("hidden_element");
})
notiBtn.addEventListener("mouseleave", () => {
    notiDes.classList.toggle("hidden_element");
})