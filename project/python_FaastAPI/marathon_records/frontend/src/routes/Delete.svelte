<script>
    let id = '';

    function delete_record(event){
        event.preventDefault()
        fetch('http://127.0.0.1:8000/delete_record', {// local 실행시 127.0.0.1으로 변환
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // 요청 본문의 유형을 JSON으로 설정
            },
            body: JSON.stringify({
                'id': id,
            })
        })
        id = ''
    }
</script>

<div class='container'>
    <h1>기록 삭제</h1>
    <form method="post" class='my-3'>
        <div class="mb-3">
            <label for="subject">기록 ID</label>
            <input type="text" class="form-control" bind:value="{id}">
        </div><br>

        <button class="btn btn-primary" on:click="{delete_record}">삭제하기</button>
    </form>
</div>