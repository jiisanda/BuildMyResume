$(document).on('click', 'confirm-delete', function(){
    return confirm('Are you sure you want to delete this resume?');
});

setTimeout(function(){
    $('.messages').remove();
  }, 4000);

$(document).on('focus', '.date-picker', function(){
    $(this).datepicker ({
        todayHighlight:true,
        dateFormat:'dd/mm/yy',
        changeMonth: true,
        changeYear: true,
        autoclose: true,
        yearRange: '1969:2030',
        defaultData: '23/07/2001',
    })
})
