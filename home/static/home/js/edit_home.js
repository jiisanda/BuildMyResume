// Certificate
var i = 0;
var div = document.getElementById('form-certi-wrap');

function addCertificateForm() {
    var clone = div.cloneNode(true);
    clone.id = "form-certi-wrap" + ++i;
    div.parentNode.appendChild(clone)
}

var btn = document.getElementById('delete-certi-btn');
btn.onclick = function() {
    document.getElementById('form-certi-wrap').remove();
    this.remove();
};

// Projects
var j = 0;
var div_proj = document.getElementById('form-project-wrap');

function addProjectForm() {
    var clone = div_proj.cloneNode(true);
    clone.id = "form-project-wrap" + ++j;
    div_proj.parentNode.appendChild(clone)
}

var btn_proj = document.getElementById('delete-project-btn');
btn_proj.onclick = function() {
    document.getElementById('form-project-wrap').remove();
    this.remove();
};
