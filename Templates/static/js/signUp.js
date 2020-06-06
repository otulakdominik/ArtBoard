var conda = 0;
$("#arrow-icon").click(function(){
  if(conda == 0){
    $(document).ready(function(){
      $("#box").css({"height":$(window).width()*0.39}, 5000);
      $("#arrow-icon").css({"transform":"scaleY(-1)"});
      $("#arrow-icon").css({"transition":"0.5s"});
      $(".options1").css({"display":"block"});
      $(".options1").css({"height":"auto"});
      $("#formatIcons").css({"display":"block"});
      conda = 1;
      
  });
  }
  else {
    $(document).ready(function(){
      $("#box").css({"height":$(window).width()*0.28}, 5000);
      $("box").css({"height":"37vw"});
      $("#arrow-icon").css({"transform":"scaleY(1)"});
      $("#arrow-icon").css({"transition":"0.5s"});
      $(".options1").css({"display":"none"});
      $(".options1").css({"height":"0"});
      $("#formatIcons").css({"display":"none"});
      conda = 0;
      
  });
  }
});
//facebook icon url
$(".fa-facebook").click(function(){
  $("#options3").css({"display":"block"});
});
// avatar icon url 
$(".fa-user-circle").click(function(){
  $("#options2").css({"display":"block"});
});
//enter confirm */
document.addEventListener("keyup", function(even) {
  if(event.keyCode == 13 || event.keyCode == 27){
    $("#options2").css({"display":"none"});
    $("#options3").css({"display":"none"});
  }
  });



var link1 = 0;
$(".fa-check-circle").click(function(){
  if(link1 == 0){
    $(document).ready(function(){
      $("#options2").css({"display":"none"});
      $("#options3").css({"display":"none"});
      console.log("XD")
      link1=1;
    });
  }
  else {
    $(document).ready(function(){
      $("#options2").css({"display":"none"});
      $("#options3").css({"display":"none"});
      link1 = 0;
      
  });
  }
});