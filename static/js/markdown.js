$(document).ready(function(){
  $(".content-markdown").each(function(){
        var content = $(this).text()
        console.log(content)
        var markedContent = marked(content)
        console.log(markedContent)
        $(this).html(markedContent)
  })
})
