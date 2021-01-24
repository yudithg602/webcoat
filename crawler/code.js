var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

var req = new XMLHttpRequest();  
req.open('GET', 'https://www.mayoclinic.org/', false);   
req.send(null);  
if(req.status == 200)
	console.log(req.responseText)
else
	console.log("error")
