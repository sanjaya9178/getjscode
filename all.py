def get_printers(request):
    data = subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\n')
    data = data[1:]
    printers = []
    for lines in data:
        for printer in lines.split("  "):
            if (printer != ""):
                printers.append(printer)
                break
    return HttpResponse(json.dumps({"printer": printers}), content_type=application_type, status=status.HTTP_200_OK)
  
  
  
  <select class="fullwidth font12" id="idselect"></select>
  
  
  function load()
{
    var idselect=document.getElementById("idselect")
    document.body.style.backgroundColor ="#f1f1f1"
    let url='/bin_labels/get_printers'
    let req=new XMLHttpRequest();
    req.onreadystatechange= function()
    {
        if(this.readyState == 4 && this.status==200)
        {
            let data=JSON.parse(req.responseText)
            for(var i=0;i<data.printer.length;i++)
            {
                var opt = document.createElement('option');
                opt.value = data.printer[i];
                opt.innerHTML = data.printer[i];
                idselect.appendChild(opt);
            }
        }
    }
    req.open("GET",url,true)
    req.send()
}




<body onload="load()">
