    $(document)
        .on('click', '.like', function () {
            var id = $(this).attr("id");
            do_like(id)
        }) // このセミコロンを削除


    function do_like(post_id) {
        $.ajax({
                url: `./${post_id}/like`,
                type: 'get'
            })
            .done((data) => {
                $('.like_list_' + post_id).html(data);
            })
    }
