$(".my-rating").starRating({
  totalStars: 5,
  starShape: 'rounded',
  starSize: 35,
  emptyColor: 'lightgray',
  hoverColor: 'salmon',
  activeColor: 'crimson',
  useGradient: false,
  minRating: 0.5,
  callback: function(currentRating, $el){
    alert('Thank you! Your rate was ' + currentRating);
    // $(this).parent().find('.input-hidden').val(currentRating)
    $('#my-input-rating').val(currentRating);
    $('#eval-button').attr('disabled', false);
    // console.log($(this).parent().find('.input-hidden').val());
    // console.log($(this).parent());
    console.log($('#my-input-rating').val());
    console.log('DOM element ', $el);
  }
});

