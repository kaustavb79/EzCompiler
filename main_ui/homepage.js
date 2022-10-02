"use strict"

function getConfig(json_file){
    $.getJSON(json_file, function(json) {        
        initTabs(json);
        $("#run").click(function(){
            alert("Submitted");
        });
    });
}

$(document).ready(function(){
    getConfig("lang_config.json");
});


function initTabs(lang_config){
    // console.log(lang_config);
    var count = 1;
    for (let key in lang_config) {
        // console.log(key, lang_config[key]);
        var btn_id = lang_config[key]+"-tab";
        var btn_target_id = "editor-"+lang_config[key];
        var btn_extension = lang_config[key];
        var btn_class = "nav-link pe-3";
        var aria_selected = false;
        if(count === 1){
            btn_class += " active";
            aria_selected = true;
        }
        var text = "<button class='"+btn_class+"' id='"+btn_id+"' data-bs-toggle='tab' data-bs-target='#"+btn_target_id+"'   type='button' role='tab' aria-controls='"+btn_extension+"' aria-selected='"+aria_selected+"'>"+key+"</button>"
        
        $("#v-pills-tab").append(text);

        updateEditor(key,btn_id,btn_target_id,btn_extension);
        count++;
    };
}

function updateEditor(lang,id,target_id,extension){
    var class_name_input = ""
    if(lang === "java"){

    }

    var editor_section = `<div class="tab-pane fade editor-segment" id="`+target_id+`" role="tabpanel" aria-labelledby="`+id+`">
        <div class="row">
            <div class="col">
                <button type="button" data-id="`+extension+`" class="btn btn-primary float-end w-25" id="run">Run</button>
            </div>
        </div>
        <div class="row editor-area">
            <div class="col">
                <div class="row mb-2">
                    <div class="col">
                        <textarea class="form-control source-code-area" id="sourceCodeArea" wrap="hard" data-id="`+extension+`" rows="15" placeholder="`+lang+`" required></textarea>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <label for="stdinArea p-10">STDIN:</label>
                        <textarea class="form-control stdin mt-2" id="stdinArea" wrap="hard" rows="4" data-id="`+extension+`" placeholder="stdin" required></textarea>
                    </div>
                </div>
            </div>
            <div class="col">
                <textarea class="form-control output-area" id="outputArea" rows="22" data-id="`+extension+`" placeholder="output" readonly></textarea>
            </div>
        </div>
    </div>`

    $(".tab-content").append(editor_section);
}


