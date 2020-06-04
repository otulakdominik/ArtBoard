var conda = 0;
$("#arrow-icon").click(function(){
  if(conda == 0){
    $(document).ready(function(){
      $("#box").css({"height":$(window).width()*0.38}, 5000);
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