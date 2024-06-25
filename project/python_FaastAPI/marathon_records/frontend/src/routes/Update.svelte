<script>
    let marathon = ''
    let date = ''
    let bibnum = ''
    let record = ''
    let dnf = ''

    function update_record(event){
        event.preventDefault()
        fetch('http://127.0.0.1:8000/update_record', { // local 실행시 127.0.0.1으로 변환
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // 요청 본문의 유형을 JSON으로 설정
            },
            body: JSON.stringify({
                "marathon": marathon,
                "date": date,
                "bibnum": bibnum,
                "record": record,
                "dnf": dnf
            })
        })
        marathon = ''
        date = ''
        bibnum = ''
        record = ''
        dnf = ''
    }

</script>

<div class="container">
    <h1 >기록 등록</h1>
    <form method="post" class="my-3">
        <div class="mb-3">
            <label for="subject">대회 이름</label>
            <input type="text" class="form-control" bind:value="{marathon}">
        </div><br>
        <div class="mb-3">
            <label for="subject">대회 일시</label>
            <input type="text" class="form-control" bind:value="{date}">
        </div><br>
        <div class="mb-3">
            <label for="subject">배번호</label>
            <input type="text" class="form-control" bind:value="{bibnum}">
        </div><br>
        <div class="mb-3">
            <label for="subject">기록</label>
            <input type="text" class="form-control" bind:value="{record}">
        </div><br>
        <div class="mb-3">
            <label for="subject">DNF 여부</label>
            <input type="text" class="form-control" bind:value="{dnf}">
        </div><br>
        
        <button class="btn btn-primary" on:click="{update_record}">저장하기</button>
    </form>
</div>
