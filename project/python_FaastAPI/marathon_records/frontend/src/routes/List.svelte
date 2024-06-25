<script>
    import { link } from 'svelte-spa-router'
    
    let record_list = []
  
    function get_record_list() {
      fetch("http://127.0.0.1:8000/records").then((response) => { // local 실행시 127.0.0.1으로 변환
        response.json().then((json) => {
          record_list = json
        })
      })
    }
  
    get_record_list()
</script>
  
<h1>기록 리스트</h1>
<ul>
    {#each record_list as record}
      <li><a use:link href="/record_detail/{record.id}">{record.marathon}{` (${record.date})`}</a></li><br>
    {/each}
</ul>
  