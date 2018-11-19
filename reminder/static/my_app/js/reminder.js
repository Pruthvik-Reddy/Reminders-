function deletereminder(reminder){
    console.log("deleting entry")
    var $reminder= $(reminder)
    $reminder.parent().remove()
    var id= $reminder.data('id')

    $.ajax(
        {
            url:'remainder/delete/'+id,
            method:'DELETE',
            beforesend:function(xhr){
                xhr.setRequestHeader('X-CSRFToken',csrf_token)
            }
        }
    )
}