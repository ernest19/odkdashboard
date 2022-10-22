$(document).ready(function(){
	$(".ajaxLoader").hide();
	$(".custom-checkbox,#priceapply").on('click',function(){
		var _filterObj={};
		var _minPrice = $("#minPrice").val();
		var _maxPrice = $("#maxPrice").val();
		_filterObj.minPrice = _minPrice;
		_filterObj.maxPrice = _maxPrice;
		$(".custom-checkbox").each(function(index,ele){
			var _filterVal = $(this).val();
			var _filterKey = $(this).data('filter');
			_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
		});

		// Run Ajax
		$.ajax({
			url:'/filter_student',
			data:_filterObj,
			dataType:'json',
			beforeSend:function(){
				$(".ajaxLoader").show();
			},
			success:function(res){
				console.log(res);
				$("#listresult").html(res.data);
				$(".ajaxLoader").hide();
			}
		});

	});
});