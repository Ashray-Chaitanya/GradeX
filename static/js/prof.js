const studName = document.getElementById("stud-name");
const  studUsn = document.getElementById("stud-usn");
fetch("/get-prof-details", {
  method: "GET",
}).then((response) => {return response.json();}).then((data) => {
  studName.textContent = `Name \t \u00A0: ${data["Name"]}`;
  studUsn.textContent = `USN\u00A0 \u00A0: ${data["USN"]}`;
});