document.addEventListener('DOMContentLoaded', function() {
    var table = document.getElementById('myTable');
    var cells = table.getElementsByTagName('td');
    
    for (var i = 0; i < cells.length; i++) {
        cells[i].addEventListener('click', function() {
            // Check if cell has a background image
            // var hasImage = this.style.td !== '<spacer> </spacer>';
            var hasNoSpacer = !this.innerHTML.includes('&nbsp;');


            // Remove highlight class from all cells
            for (var j = 0; j < cells.length; j++) {
                cells[j].classList.remove('highlight');
            }
            
            // Add highlight class to clicked cell
            if (hasNoSpacer) {
                this.classList.add('highlight');
            }
        });
    }
});