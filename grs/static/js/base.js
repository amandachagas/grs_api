$(".my-rating").starRating({
  totalStars: 5,
  starShape: 'rounded',
  starSize: 35,
  emptyColor: 'lightgray',
  hoverColor: 'salmon',
  activeColor: 'crimson',
  useGradient: false,
  minRating: 0.5,
  disableAfterRate: false,
  callback: function(currentRating, $el){
    
    $el.parent('form').children('input[name=this-rating]').val(currentRating);
    $el.parent('form').children('span[name=text-rating]').text(currentRating);
    // $el.parent('form').children('button[name=this-button]').attr('disabled', false);

    console.log($el.parent('form').children('input[name=this-rating]').val());

    $el.parent('form').submit();

  },
  // onHover: function(currentIndex, currentRating, $el){
  //   $(".my-rating").starRating('setRating', 0);
  //   $(".my-rating").starRating('setRating', currentRating);
  // },
});


$('.eval-form').submit(function(e){
  var form = $(this);
  var url = "/";
  e.preventDefault();

  $.ajax({
    method: "post",
    url: url,
    data: form.serialize(),
    dataType: 'json',

    beforeSend: function(){
        //$(".container_loader_ajax").css("display","block");
    },
    complete: function(){
        //$(".container_loader_ajax").css("display","none");
        // console.log(form.children());

        // form.children('button[name=this-button]').attr('disabled', true);
    },
    success: function( data ) {
      form.parent().parent().css("background", "rgba(0, 255, 0, 0.2)");
      // $("#form-messages").html('<div class="submit-status-text"><span class="success"><i class="ion ion-ios-checkmark-outline"></i> ' + data.data[0].mensagem + '</span></div>').fadeIn(300).delay(3000).fadeOut(300);             
    },
    error: function(x, y){
      form.parent().parent().css("background", "rgba(255, 0, 0, 0.2)");
      // $("#form-messages").html('<div class="submit-status-text"><span class="error"><i class="ion ion-ios-close-outline"></i> ' + data.data[0].erro + ' ' + data.data[0].erro + '</span></div>').fadeIn(300).delay(3000).fadeOut(300);
      console.log(x)
      console.log(y)              
    }
  });

});


$('.csv-form').submit(function(e){
  var form = $(this);
  var url = "to_csv/";
  e.preventDefault();

  $.ajax({
    method: "post",
    url: url,
    data: form.serialize(),
    dataType: 'json',
    complete: function(){

    },
    success: function( data ) {
      alert('ok');
    },
    error: function(x, y){
      console.log(x)
      console.log(y)              
    }
  });

});