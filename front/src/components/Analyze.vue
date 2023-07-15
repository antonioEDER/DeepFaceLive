<template>
  <div class="q-ma-lg">
    <div class="q-pa-md">
      <div class="q-gutter-md">
        <q-form @submit="onSubmit">
          <label for="diretorio">Selecione uma foto</label>
          <q-file required @input="() => deepface = []" filled v-model="diretorio" label="Diretório" />

          <q-btn :loading="submitting" color="green" class="q-mt-md" type="submit" label="Enviar" />
        </q-form>
        <div v-for="(face, index) in deepface" :key="index">
          <q-card class="my-card">

            <div id="imageContainer">
              <img id="image" class="img" :src="img">
              <div id="highlight"></div>
            </div>

            <div>
              <q-card-section>
                <div class="text-h6">{{ this.diretorio.name }}</div>
                <div class="text-subtitle2">Analize da foto</div>
              </q-card-section>

              <q-card-section>
                <div class="text-bold text-red">Idade: {{ face.age }}</div>
              </q-card-section>

              <q-card-section class="q-pt-none">
                <div class="text-bold">Emoções</div>
                <div>Nervosa: {{ parseFloat(face.emotion.angry).toFixed(1) }}%</div>
                <div>Desgosto: {{ parseFloat(face.emotion.disgust).toFixed(1) }}%</div>
                <div>Medo: {{ parseFloat(face.emotion.fear).toFixed(1) }}%</div>
                <div>Feliz: {{ parseFloat(face.emotion.happy).toFixed(1) }}%</div>
                <div>Triste: {{ parseFloat(face.emotion.sad).toFixed(1) }}%</div>
                <div>Surpreso: {{ parseFloat(face.emotion.surprise).toFixed(1) }}%</div>
                <div>Neutro: {{ parseFloat(face.emotion.neutral).toFixed(1) }}%</div>
                <div class="text-bold text-red">Predominância: {{ dominantEmotion(face.dominant_emotion) }} </div>
              </q-card-section>

              <q-card-section>
                <div class="text-bold">Gênero</div>
                <div>Mulher: {{ parseFloat(face.gender.Woman).toFixed(1) }}%</div>
                <div>Homem: {{ parseFloat(face.gender.Man).toFixed(1) }}%</div>
                <div class="text-bold text-red">Predominância: {{ face.dominant_gender === 'Man' ? 'Homem' : 'Mulher' }}
                </div>
              </q-card-section>

              <q-card-section>
                <div class="text-bold">Raça</div>
                <div>Asiático: {{ parseFloat(face.race.asian).toFixed(1) }}%</div>
                <div>Indiano: {{ parseFloat(face.race.indian).toFixed(1) }}%</div>
                <div>Negro: {{ parseFloat(face.race.black).toFixed(1) }}%</div>
                <div>Branco: {{ parseFloat(face.race.white).toFixed(1) }}%</div>
                <div>Oriental: {{ parseFloat(face.race["middle eastern"]).toFixed(1) }}%</div>
                <div>Latino hispânico: {{ parseFloat(face.race["latino hispanic"]).toFixed(1) }}%</div>
                <div class="text-bold text-red">Predominância: {{ dominantRace(face.dominant_race) }} </div>
              </q-card-section>
            </div>

          </q-card>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PagAnalyze',
  data () {
    return {
      diretorio: {},
      img: null,
      api: 'http://localhost:8000',
      storage: 'http://localhost:3000/',
      deepface: null,
      submitting: false,
    }
  },
  methods: {
    dominantEmotion (emotion) {
      let dominant = ""
      switch (emotion) {
        case "angry":
          dominant = "Nervosa"
          break;
        case "disgust":
          dominant = "Desgosto"
          break;
        case "fear":
          dominant = "Medo"
          break;
        case "happy":
          dominant = "Feliz"
          break;
        case "sad":
          dominant = "Triste"
          break;
        case "surprise":
          dominant = "Surpreso"
          break;
        case "neutral":
          dominant = "Neutro"
          break;
        default:
          break;
      }
      return dominant
    },
    dominantRace (race) {
      let dominant = ""
      switch (race) {
        case "asian":
          dominant = "Asiático"
          break;
        case "indian":
          dominant = "Indiano"
          break;
        case "black":
          dominant = "Negro"
          break;
        case "white":
          dominant = "Branco"
          break;
        case "middle eastern":
          dominant = "Oriental"
          break;
        case "latino hispanic":
          dominant = "Latino hispânico"
          break;
        default:
          break;
      }
      return dominant
    },
    convertAndInsertImage (file) {
      const self = this
      var reader = new FileReader();
      reader.onload = function(e) {
        var dataURL = e.target.result;
        self.img = dataURL;
      };
      reader.readAsDataURL(file);
    },
    setDimensionsImg () {
      var highlight = document.getElementById('highlight');
      var highlightData = this.deepface[0].region;
      highlight.style.left = highlightData.x + 'px';
      highlight.style.top = highlightData.y + 'px';
      highlight.style.width = highlightData.w + 'px';
      highlight.style.height = highlightData.h + 'px';
    },
    onSubmit () {
      this.submitting = true
      this.deepface = []

      const formData = new FormData();
      formData.append('file', this.diretorio);

      const headers = { 'Content-Type': 'multipart/form-data' };
        
      axios.post(`${this.api}/analyze`, formData, { headers })
        .then((response) => {
          this.deepface = response.data
          setTimeout(() => {
            this.setDimensionsImg()
          }, 1000);
        })
        .finally(() => {
          this.submitting = false
          this.convertAndInsertImage(this.diretorio)
        })
    }
  },
}
</script>

<style scoped>
.my-card {
  display: grid;
  grid-template-columns: 400px 1fr;
}
.img {
  width: auto;
  height: auto;
}

#imageContainer {
  position: relative;
  display: inline-block;
}
    
#highlight {
  position: absolute;
  border: 4px solid red;
}
</style>