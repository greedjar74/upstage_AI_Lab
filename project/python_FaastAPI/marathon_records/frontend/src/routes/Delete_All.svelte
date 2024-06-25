<script>
    let confirm = '';

    function delete_all(event){
        event.preventDefault()
        if(confirm === 'Delete All') {
            fetch('http://127.0.0.1:8000/delete_all') // local 실행시 127.0.0.1으로 변환
            confirm = ''
        }
    }

</script>

<div class='container'>
    <h1>기록 전체 삭제</h1>
    <h3>전체 기록를 원하시면 'Delete All'을 입력하세요.</h3>
    <div class="mb-3">
        <input type="text" class="form-control" bind:value="{confirm}">
    </div><br>

    <button class="btn btn-primary" on:click="{delete_all}">기록 전체 삭제</button>
</div>