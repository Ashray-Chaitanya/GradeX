document.getElementById('myForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission

  const usn = document.getElementById('USN').value;

  // Send the form data via AJAX
  fetch('/login-complete', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ USN: usn })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      const tableBody = document.getElementById('tableBody');
      tableBody.innerHTML = ''; // Clear existing table rows
      data.students.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${row[0]}</td>
          <td>${row[1]}</td>
          <td>${row[2]}</td>
          <td>${row[3]}</td>
          <td>${row[4]}</td>
        `;
        tableBody.appendChild(tr);
      });
      document.getElementById('myTable').style.display = 'table';
      document.getElementById('tableHeaders').style.display = 'table-header-group';
      tableBody.style.display = 'table-row-group';

      // Show the print button after data is populated
      document.getElementById('printButton').classList.remove('hidden');
      document.getElementById('Analyze').classList.remove('hidden');

    } else {
      alert('No data found for the entered USN.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
});


function printData() {
  // Hide unnecessary elements (optional)
  const elementsToHide = document.querySelectorAll('.logo, .header, form');
  elementsToHide.forEach(element => {
    element.style.display = 'none';
  });

  // Trigger the print dialog
  window.print();

  // Restore hidden elements (optional)
  setTimeout(() => {
    elementsToHide.forEach(element => {
      element.style.display = '';
    });
  }, 1000); 

}


