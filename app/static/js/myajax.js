function myajax(type,url,data,successfn,errorfn) {
    $.ajax({
        type: type,
        url: url,
        data: data,
        dataType: "json",
        success: function(data){
	    successfn(data)
    },
        error: function(){
	    errorfn()
    },

    })
    
}
