<template>
    <div class="searchBox">
        
        <p style="text-align:left; color:white; font-size:30px;">#추천태그</p><hr>
            <div class="search" >
                <div class=tagGroup>
                        <b-button
                            v-for="(btn, idx) in buttons"
                            :key="idx"
                            :pressed.sync="btn.state"
                            variant="outline-light"
                        >
                            {{ btn.caption }}
                        </b-button>
                        <!-- <p>Pressed States: <strong>{{ btnStates }}</strong></p> -->
                </div>
                <div class="searchButton">
                    <b-button block class="button">word로 검색</b-button>
                    <b-button block class="button" variant="danger">검색하기</b-button>
                </div>
            </div>
        
    </div>
</template>
<script>
export default {
    data() {
        return {
            buttons: [
                {caption: '#가족들과 가기 좋은', state: false},
                {caption: '#물놀이 하기 좋은', state: false},
                {caption: '#봄', state: false},
                {caption: '#바다가 보이는', state: false},
                {caption: '#반려견 동반', state: false},
                {caption: '#문화유적', state: false},
                {caption: '#산이 보이는', state: false},
                {caption: '#계곡옆', state: false},
                {caption: '#익스트림', state: false},
                {caption: '#생태교육', state: false},
                {caption: '#별 보기 좋은', state: false},
            ]
        }
    },
    computed: {
      btnStates() {
        return this.buttons.map(btn => btn.state)
      }
    }
}
</script>
<style scoped>
.searchBox{
    width: 100%;
    height: 70vh;
    background-image: url("../../assets/SearchPageImage2.jpg");
    background-repeat: no-repeat; 
    background-size: cover;
    background-position: center; 
    padding: 10%;
}

.search {
    display: flex;
    
}
.tagGroup {
    float: left;
    width:70%;
    box-sizing: border-box;
}
.searchButton {
    float: left;
    margin: 0px 5%;
    width:30%;
    box-sizing: border-box;
} 

button {
    margin: 0 1% 8px 0;
}

hr {
  background-color: white;
}
</style>