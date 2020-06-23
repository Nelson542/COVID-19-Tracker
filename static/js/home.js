retrieve_state();
function retrieve_state() {
    var table = document.getElementById('display-table');
    var cells = table.getElementsByTagName('td');

    for (var i = 0; i < cells.length; i++) {
        var cell = cells[i];
        cell.onclick = function () {
            var rowId = this.parentNode.rowIndex;
            var rowSelected = table.getElementsByTagName('tr')[rowId];
            var state = rowSelected.cells[0].innerHTML;

             $.ajax(
                {
                    type:'POST',
                    contentType:'application/json;charset-utf-08',
                    dataType:'json',
                    url:'/state?value='+state ,
                    success:function (data) {
                        var reply=data.reply;
                        if (reply=="success")
                        {
                            window.location.href = '/display';
                        }
                        else
                        {
                            alert("some error occured in session agent")
                        }
                    }
                }
            );
        }
    }
}

function search() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("display-table");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}




