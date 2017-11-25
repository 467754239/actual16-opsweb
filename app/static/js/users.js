function checkuser(username){
        if ( username == '' ) {
                $('#checkuserinfo').html('Username is null')
                return false
        }
        else {
                $('#checkuserinfo').html('')
        }
        return true
}

function checkemail(email){
        if ( email == '' ) {
                $('#checkemailinfo').html('Email is null')
                return false
        }
        else {
                $('#checkemailinfo').html('')
        }

        var re =  /^(\w)+(\.\w+)*@51reboot\.com$/;
        if (!re.test(email)) {
               $('#checkemailinfo').html('This email format is not correct. Please use *@51reboot\.com.')
               return false

        }
        return true

}

function checkpasswd(password){
        if ( password == '' ) {
                $('#checkpasswd').html('Password is null')
                return false
        }
        else {
                $('#checkpasswd').html('')
        }
        return true
}

function checkrpasswd(rpassword){
        if ( rpassword == '' ) {
                $('#comparepasswd').html('Confirm password is null')
                return false
        }
        else {
                $('#comparepasswd').html('')
        }
        return true
}


$('#editbtnclose').click(function(){
          $('#username').attr('value','')
          $('#email').attr('value','')
          $('#password').attr('value','')
          $('#rpassword').attr('value','')
})

$('.editbtn').click(function(){
        console.log('edit')
        var id = $(this).attr('uid')
        var username = $(this).parents('tr').children('td').eq(1).text()
        var email = $(this).parents('tr').children('td').eq(2).text()
        var password = $(this).parents('tr').children('td').eq(3).text()

        $('#myModal').modal('show')

        $('#username').attr('value',username.trim())
        $('#email').attr('value',email.trim())
        $('#password').attr('value',password.trim())
        $('#rpassword').attr('value',password.trim())

	$('#btnsave').click(function(){
                var username = $('#username').val().trim()
                var email = $('#email').val().trim()
                var password = $('#password').val().trim()
                var rpassword = $('#rpassword').val().trim()

                if (!checkuser(username))
                            return

                if (!checkemail(email))
                    return

                if (!checkpasswd(password))
                    return

                if (!checkrpasswd(rpassword))
                    return
		if ( password != rpassword ) {
                        $('#comparepasswd').html('The password and confirm password are different!')
                        return
                }
                else {
                        $('#comparepasswd').html('')
                }


                type = 'POST'
                url = '/users/edit/' + id
                data = {username:username,email:email,password:password,id:id}

                function successfn(data) {
                    location.reload()
                }

                function errorfn() {
                        $('#errorstatus').html('Sorry. The server has an exception!')
                }
                myajax(type,url,data,successfn,errorfn)

      })
$('#username').change(function(){
        var username = $('#username').val().trim()
        console.log('username change')

        if (!checkuser(username))
    	    return

        type = 'POST'
        url = '/checkuser' 
        data = {username:username}
        
        function successfn1(data) {
    	    console.log('successfn111111')
    	    console.log(data)
    	    if (data['status'] == 1) {
                    $('#checkuserinfo').html('This user exist. Please change another username!')
    		  //  $('#btnsave').attr('disabled',true)
    		    return false
    	    }
    	    else {
    	    console.log('user no exist')
                $('#checkuserinfo').html('')
		console.log('enale disabled')
		//$('#btnsave').attr('disabled',false)
    	    }

        }
        
        function errorfn1() {
    	    console.log('ajax error')
                $('#errorstatus').html('Sorry. The server has an exception!')
        }

        myajax(type,url,data,successfn1,errorfn1)

})

$('#email').change(function(){
        var email = $('#email').val().trim()
        if (!checkemail(email))
    	    return

        type = 'POST'
        url = '/checkemail' 
        data = {email:email}

        function successfn2(data) {
    	    if (data['status'] == 1) {
    	            $('#checkemailinfo').html('This email exist. Please change another email!')
    		    //$('#btnsave').attr("disabled","true")
    		    return false
    	    }
    	    else {
    	        $('#checkemailinfo').html('')
    		//$('#btnsave').attr("disabled","false")
    	    }

        }
        
        function errorfn2() {
                $('#errorstatus').html('Sorry. The server has an exception!')
        }

        myajax(type,url,data,successfn2,errorfn2)


})

$('#password').change(function(){
        var password = $('#password').val().trim()
        if (!checkpasswd(password))
    	    return

})

$('#rpassword').change(function(){
        var password = $('#password').val().trim()
        var rpassword = $('#rpassword').val().trim()
        if (!checkrpasswd(rpassword))
    	    return

        if ( password != rpassword ) {
    	    $('#comparepasswd').html('The password and confirm password are different!')
    	    return
        }
        else {
    	    $('#comparepasswd').html('')
        }


})

})
          


//$('#username').change(function(){
//        var username = $('#username').val().trim()
//        console.log('username change')
//
//        if (!checkuser(username))
//    	    return
//
//        type = 'POST'
//        url = '/checkuser' 
//        data = {username:username}
//        
//        function successfn1(data) {
//    	    console.log('successfn111111')
//    	    console.log(data)
//    	    if (data['status'] == 1) {
//                    $('#checkuserinfo').html('This user exist. Please change another username!')
//    		  //  $('#btnsave').attr('disabled',true)
//    		    return false
//    	    }
//    	    else {
//    	    console.log('user no exist')
//                $('#checkuserinfo').html('')
//		console.log('enale disabled')
//		//$('#btnsave').attr('disabled',false)
//    	    }
//
//        }
//        
//        function errorfn1() {
//    	    console.log('ajax error')
//                $('#errorstatus').html('Sorry. The server has an exception!')
//        }
//
//        myajax(type,url,data,successfn1,errorfn1)
//
//})
//
//$('#email').change(function(){
//        var email = $('#email').val().trim()
//        if (!checkemail(email))
//    	    return
//
//        type = 'POST'
//        url = '/checkemail' 
//        data = {email:email}
//
//        function successfn2(data) {
//    	    if (data['status'] == 1) {
//    	            $('#checkemailinfo').html('This email exist. Please change another email!')
//    		    $('#btnsave').attr("disabled","true")
//    		    return false
//    	    }
//    	    else {
//    	        $('#checkemailinfo').html('')
//    		$('#btnsave').attr("disabled","false")
//    	    }
//
//        }
//        
//        function errorfn2() {
//                $('#errorstatus').html('Sorry. The server has an exception!')
//        }
//
//        myajax(type,url,data,successfn2,errorfn2)
//
//
//})
//
//$('#password').change(function(){
//        var password = $('#password').val().trim()
//        if (!checkpasswd(password))
//    	    return
//
//})
//
//$('#rpassword').change(function(){
//        var password = $('#password').val().trim()
//        var rpassword = $('#rpassword').val().trim()
//        if (!checkrpasswd(rpassword))
//    	    return
//
//        if ( password != rpassword ) {
//    	    $('#comparepasswd').html('The password and confirm password are different!')
//    	    return
//        }
//        else {
//    	    $('#comparepasswd').html('')
//        }
//

//})

//$('#btnsave').click(function(){
//        var username = $('#username').val().trim()
//        var email = $('#email').val().trim()
//        var password = $('#password').val().trim()
//        var rpassword = $('#rpassword').val().trim()
//
//        if (!checkuser(username))
//		    return
//
//        if (!checkemail(email))
//    	    return
//
//        if (!checkpasswd(password))
//    	    return
//
//        if (!checkrpasswd(rpassword))
//    	    return
//
//        type = 'POST'
//        url = '/users/edit/' + id
//        data = {username:username,email:email,password:password,id:id}
//
//        function successfn(data) {
//    	    location.reload()
//        }
//
//        function errorfn() {
//                $('#errorstatus').html('Sorry. The server has an exception!')
//        }
//        myajax(type,url,data,successfn,errorfn)
//
//})


$('.delbtn').click(function(){
    $('#myDelModal').modal('show')
    var uid = $(this).attr('uid')
    var name = $(this).attr('username')
    $('#delinfo').html('你确定要删除 ' + name + ' 用户吗?')

    $('#btndel').click(function(){

    	    type = 'POST'
    	    url = '/users/del/' + uid
    	    data = {}
    	    function successfn3(data) {
    	            location.reload()

    	    }
    	    
    	    function errorfn3() {
    		    console.log('del ajax error')
    	    }

                    myajax(type,url,data,successfn3,errorfn3)

    })
       
})

