function addRow() {
    const tableBody = document.getElementById('timetable-body');
    const newRow = document.createElement('tr');

    // Time cell
    const timeCell = document.createElement('td');
    timeCell.textContent = prompt('Enter time slot (e.g., 3:00 - 4:00):', '3:00 - 4:00');
    newRow.appendChild(timeCell);

    // Days cells
    for (let i = 0; i < 5; i++) {
        const dayCell = document.createElement('td');
        dayCell.textContent = prompt(`Enter subject for ${['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'][i]}:`, 'New Subject');
        newRow.appendChild(dayCell);
    }

    tableBody.appendChild(newRow);
}
