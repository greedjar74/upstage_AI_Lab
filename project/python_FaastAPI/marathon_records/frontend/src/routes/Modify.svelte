<script>
    let id = '';
    let col = '';
    let data = '';

    function update_record(event){
        event.preventDefault()
        fetch('http://127.0.0.1:8000/modify_record', { // local 실행시 127.0.0.1으로 변환
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // 요청 본문의 유형을 JSON으로 설정
            },
            body: JSON.stringify({
                'id': id,
                'col': col,
                'data': data
            })
        })
        id = ''
        col = ''
        data = ''
    }
</script>

<div class='container'>
    <h1>기록 수정</h1>
    <form method="post" class='my-3'>
        <div class="mb-3">
            <label for="subject">기록 ID</label>
            <input type="text" class="form-control" bind:value="{id}">
        </div><br>
        <div class="mb-3">
            <label for="subject">변경 요소</label>
            <input type="text" class="form-control" bind:value="{col}">
        </div><br>
        <div class="mb-3">
            <label for="subject">변경 값</label>
            <input type="text" class="form-control" bind:value="{data}">
        </div><br>

        <button class="btn btn-primary" on:click="{update_record}">저장하기</button>
    </form>
</div>