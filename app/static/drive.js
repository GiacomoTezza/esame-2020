$(document).ready(function () {
    // function that let table rows be clickable
    $(document).on('click', 'tr.subscriber', function () {
        var personID = $(this).attr('data-person-id');
        window.location.href = `/client/${personID}`;
    });


    $(document).on('click', 'tr.exam', function () {
        var license = $(this).attr('data-license-id');
        var client = $(this).attr('data-client-id');
        var date = $(this).attr('data-date-id');

        var url = '/exam';
        var form = $(
            '<!-- im the hackerman -->' +
            '<form hidden action="' + url + '" method="post">' +
            '<input type="text" name="LicenseID" value=' + license + ' />' +
            '<input type="text" name="ClientID" value=' + client + ' />' +
            '<input type="text" name="StartDate" value=' + date + ' />' +
            '</form>');
        $('body').append(form);
        form.submit();
    });

    // Filters
    $("#SurnameFilter").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#FilteredTable tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $("#NameFilter").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#FilteredTable tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $("#LicenseFilter").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#FilteredTable tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $("#StatusFilter").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#FilteredTable tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $("#DateFilter").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#FilteredTable tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});