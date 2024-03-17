document.addEventListener("DOMContentLoaded", load);
function load() {
  fetch("/room")
    .then((response) => response.json())
    .then((data) => {
      console.log(data.rooms);
      data.rooms.forEach(show);
    });
}
function show(rooms) {
  const roomDiv = document.getElementById("rooms");
  const room = document.createElement("div");

  room.innerHTML = `Name: ${rooms.name} Students: ${rooms.student_count} Teacher: ${rooms.teacher.user.username }`;

  roomDiv.appendChild(room);
}
