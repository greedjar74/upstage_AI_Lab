<script>
    import { link } from 'svelte-spa-router';
</script>

<h1>마라톤 기록</h1>
<h3>
    <button class="btn btn-primary"><a use:link href="/records">기록 확인</a></button><br>
    <button class="btn btn-primary"><a use:link href="/update_record">기록 등록</a></button><br>
    <button class="btn btn-primary"><a use:link href="/modify_record">기록 수정</a></button><br>
    <button class="btn btn-primary"><a use:link href="/delete_record">기록 삭제</a></button><br>
    <button class="btn btn-primary"><a use:link href="/delete_all">기록 전체 삭제</a></button>
</h3>