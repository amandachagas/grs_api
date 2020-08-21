$(".my-rating-4").starRating({
  totalStars: 5,
  starShape: 'rounded',
  starSize: 40,
  emptyColor: 'lightgray',
  hoverColor: 'salmon',
  activeColor: 'crimson',
  useGradient: false,
  minRating: 0.5,
  callback: function(currentRating, $el){
    alert('rated ' + currentRating);
    console.log('DOM element ', $el);
  }
});