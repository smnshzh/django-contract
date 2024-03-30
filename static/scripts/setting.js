       document.addEventListener('DOMContentLoaded', function() {
            var jsonData;
            var chunkSize = 5;
            var currentPage = 1;
            // Loading spinner
            var loadingSpinner = document.getElementById('loadingSpinner');
            // Add event listener to file input
            document.getElementById('excel_file').addEventListener('change', function(event) {
                var file = event.target.files[0];
                var reader = new FileReader();
                // Show loading spinner
                loadingSpinner.classList.remove('hidden');
                reader.onload = function(e) {
                    var data = new Uint8Array(e.target.result);
                    var workbook = XLSX.read(data, {type: 'array'});
                    var sheetName = workbook.SheetNames[0];
                    var sheet = workbook.Sheets[sheetName];
                    jsonData = XLSX.utils.sheet_to_json(sheet, {header: 1});
                    // Hide loading spinner
                    loadingSpinner.classList.add('hidden');
                    // Show table container
                    document.getElementById('tableContainer').classList.remove('hidden');

                    renderPage(currentPage);
                };

                reader.readAsArrayBuffer(file);
            });

            function renderPage(pageNumber) {
                var startIndex = (pageNumber - 1) * chunkSize;
                var endIndex = startIndex + chunkSize;
                var chunkData = jsonData.slice(startIndex, endIndex);

                var table = document.createElement('table');
                table.className = 'w-full border-collapse border border-gray-300';
                var thead = document.createElement('thead');
                var tbody = document.createElement('tbody');

                // Generate table headers
                var headerRow = document.createElement('tr');
                for (var i = 0; i < jsonData[0].length; i++) {
                    var th = document.createElement('th');
                    th.textContent = jsonData[0][i];
                    th.className = 'border border-gray-300 p-2';
                    headerRow.appendChild(th);
                }
                thead.appendChild(headerRow);

                // Generate table rows
                for (var j = 1; j < chunkData.length; j++) {
                    var row = document.createElement('tr');
                    for (var k = 0; k < chunkData[j].length; k++) {
                        var cell = document.createElement('td');
                        cell.textContent = chunkData[j][k];
                        cell.className = 'border border-gray-300 p-2';
                        row.appendChild(cell);
                    }
                    tbody.appendChild(row);
                }
                table.appendChild(thead);
                table.appendChild(tbody);

                // Clear previous pagination
                document.getElementById('paginationContainer').innerHTML = '';
                // Append table to pagination container
                document.getElementById('paginationContainer').appendChild(table);

                // Update pagination buttons
                updatePaginationButtons(pageNumber);
            }

            function updatePaginationButtons(currentPage) {
                var prevButton = document.getElementById('prevButton');
                var nextButton = document.getElementById('nextButton');

                if (currentPage === 1) {
                    prevButton.disabled = true;
                } else {
                    prevButton.disabled = false;
                }

                if (currentPage === Math.ceil(jsonData.length / chunkSize)) {
                    nextButton.disabled = true;
                } else {
                    nextButton.disabled = false;
                }
            }

            document.getElementById('prevButton').addEventListener('click', function() {
                if (currentPage > 1) {
                    currentPage--;
                    renderPage(currentPage);
                }
            });

            document.getElementById('nextButton').addEventListener('click', function() {
                if (currentPage < Math.ceil(jsonData.length / chunkSize)) {
                    currentPage++;
                    renderPage(currentPage);
                }
            });


        });