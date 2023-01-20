// $(document).ready(function(){
	// $(".ajaxLoader").hide();
	function runfilter(){
		var _filterObj={};
		var _minAge = $("#minAge").val();
		var _maxAge = $("#maxAge").val();
		_filterObj.minPrice = _minAge;
		_filterObj.maxPrice = _maxAge;
		$(".filter").each(function(index,ele){
			var _filterVal = $(this).val();
			console.log(_filterVal)
			// var _filterKey = $(this).data('filter');
			// _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			//  	return el.value;
			// });
		});

		// Run Ajax
		$.ajax({
			url:'/chartsPlot/',
			data:_filterObj,
			dataType:'json',
			beforeSend:function(){
				$(".ajaxLoader").show();
			},
			success:function(res){
				console.log(res);
				// $("#listresult").html(res.data);
				// $(".ajaxLoader").hide();
			}
		});
	}
	// });
