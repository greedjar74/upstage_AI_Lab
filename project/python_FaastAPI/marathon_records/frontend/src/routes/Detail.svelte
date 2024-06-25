<script>
    export let params = {}
    let record_id = params.record_id
    let record_detail = {}

    function get_record_detail() {
        fetch(`http://127.0.0.1:8000/record_detail/${record_id}`).then((response) => {// local 실행시 127.0.0.1으로 변환
            response.json().then((json) => {
                record_detail = json
            })
        })
    }

    get_record_detail()
</script>

<h1>{record_detail.marathon}</h1>
<div>
    {`대회 일시: ${record_detail.date}`}<br><br>
    {`배번호: ${record_detail.bibnum}`}<br><br>
    {`기록: ${record_detail.record}`}<br><br>
    {`DNF했나요? ${record_detail.dnf}`}<br><br>
</div>