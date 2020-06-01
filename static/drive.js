$(document).ready(function () {
    $(document).on('click', 'tr.clickable', function () {
        var personID = $(this).attr('data-person-id');
        window.location.href = `/client/${personID}`;
    });
});