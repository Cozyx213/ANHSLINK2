document.addEventListener("DOMContentLoaded", load);
function load() {
  fetch("/room")
    .then((response) => response.json())
    .then((data) => {
      console.log(data.rooms);
      data.rooms.length != 0 ? console.log("naa") : console.log("wala");
      data.rooms.forEach(show);
    });
}
function show(rooms) {
  const roomDiv = document.getElementById("rooms");
  const room = document.createElement("div");
  console.log(rooms);
  room.innerHTML =
    rooms && Object.keys(rooms).length > 0
      ? `
      
      <div class="bg-black"></div>
      Name: ${rooms.name} Students: ${rooms.student_count} Teacher: ${rooms.teacher.user.username}`
      : `waysud`;
  roomDiv.appendChild(room);
}
