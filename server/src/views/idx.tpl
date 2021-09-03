<html>
<body style="background-color:#343a40 !important;">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
    <script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>
    <table class="sortable table table-hover table-striped table-bordered" style="width:100%">
        <tr>
            <th class="text-light">character</th>
            <th class="text-light">realm</th>
            <th class="text-light">class</th>
            <th class="text-light">ilvl</th>
            <th class="text-light">dungeon</th>
            <th class="text-light">level</th>
        </tr>
        % for character in characters:
        % if character.dungeon_reset_time > time:
        <tr {{!row_color(character)}}>
            <td>{{str(character.character_name)}}</td>
            <td>{{str(character.character_realm)}}</td>
            <td>{{str(character.character_class)}}</td>
            <td>{{str(character.character_item_level)}}</td>
            <td>{{str(character.dungeon_name)}}</td>
            <td>{{str(character.dungeon_level)}}</td>
        </tr>
        % end
        % end
    </table>
</body>
</html>