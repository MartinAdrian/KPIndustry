let domain_address = "http://127.0.0.1:8000"

function projectRedirect() {
      var project_ids = document.querySelectorAll("[id='project_redirect']");
      var project_id = 0
      for(var i = 0; i < project_ids.length; i++){
        console.log(typeof project_ids[i].value)
        if(project_ids[i].value != "-- Projects list --"){
            console.log("inside if");
            project_id = project_ids[i].value;
            break;
        }
      };
      var link = `${domain_address}/KPIndustry/${project_id}/manage-project/`
      window.location.href = link;
    }