//init stack
var stack_undo = [];
var stack_redo = [];

//disable button
$("#btn-redo").attr("disabled", true);
$("#btn-undo").attr("disabled", true);


//check disable button
function ckeck_disable_button(){
    if(stack_redo.length == 0)
        $("#btn-redo").attr("disabled", true);
    else
        $("#btn-redo").attr("disabled", false);

    if(stack_undo.length == 0)
        $("#btn-undo").attr("disabled", true);
    else
        $("#btn-undo").attr("disabled", false);
}


//undo
function undo(){
    if(stack_undo.length > 0){
        var content = $('#text').val();
        var word = stack_undo.pop();
        stack_redo.push(word);
        var index = content.lastIndexOf(word);
        new_content = content.substr(0,index);
        console.log(stack_undo);
        $('#text').val(new_content);
        ckeck_disable_button();
    }
}

//rredo
function redo(){
    if(stack_redo.length > 0){
        var content = $('#text').val();
        var index = content.lastIndexOf(" ");
        new_content = content.substr(0,index);
        var word = stack_redo.pop();
        stack_undo.push(word);
        new_content += " " + word;
        $('#text').val(new_content);
        ckeck_disable_button();
    }
    
}

//get key on textarea
$('#text').keyup(function(e){
    var content = $('#text').val();
    var check = content.endsWith(". ") || content.endsWith(', ')
    if (e.keyCode == 32 && !check){
        var content = $('#text').val();
        var arr = content.split(' ');
        stack_undo.push(arr[arr.length-2] + " ");
        stack_redo = [];
        console.log(stack_undo);     
    }
    if (e.keyCode == 190 || e.keyCode == 188){
        var content = $('#text').val();
        var arr = content.split(' ');
        stack_undo.push(arr[arr.length-1] + " ");
        stack_redo = [];
        console.log(stack_undo);
    }
    ckeck_disable_button();
})
