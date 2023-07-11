<template>
  <div class="q-ma-lg">
    <div class="q-pa-md" style="max-width: 300px">
      <div class="q-gutter-md">
        <q-form @submit="onSubmit">
          <label for="diretorio">Selecione uma foto</label>
          <q-file filled v-model="diretorio" label="Diretório" />

          <q-btn :loading="submitting" color="green" class="q-mt-md" type="submit" label="Enviar" />
        </q-form>
        <div v-for="(face, index) in deepface" :key="index">
          <q-card class="my-card">
            <img :src="this.storage + this.diretorio.name">

            <q-card-section>
              <div class="text-h6">{{ this.diretorio.name }}</div>
              <div class="text-subtitle2">Analize da foto</div>
            </q-card-section>

            <q-card-section>
              <div>Idade:{{ face.age }}</div>
            </q-card-section>

            <q-card-section class="q-pt-none">
              <div class="text-bold">Emoções</div>
              <div>Raiva:{{ parseFloat(face.emotion.angry).toFixed(1) }}%</div>
              <div>Desgosto:{{ parseFloat(face.emotion.disgust).toFixed(1) }}%</div>
              <div>Medo:{{ parseFloat(face.emotion.fear).toFixed(1) }}%</div>
              <div>Feliz:{{ parseFloat(face.emotion.happy).toFixed(1) }}%</div>
              <div>Triste:{{ parseFloat(face.emotion.sad).toFixed(1) }}%</div>
              <div>Surpreso:{{ parseFloat(face.emotion.surprise).toFixed(1) }}%</div>
              <div>Neutro:{{ parseFloat(face.emotion.neutral).toFixed(1) }}%</div>
              <div class="text-bold text-red">Predominância: {{ face.dominant_emotion }} </div>
            </q-card-section>

            <q-card-section>
              <div class="text-bold">Gênero</div>
              <div>Mulher:{{ parseFloat(face.gender.Woman).toFixed(1) }}%</div>
              <div>Homem:{{ parseFloat(face.gender.Man).toFixed(1) }}%</div>
              <div class="text-bold text-red">Predominância: {{ face.dominant_gender }} </div>
            </q-card-section>

            <q-card-section>
              <div class="text-bold">Raça</div>
              <div>Asiático:{{ parseFloat(face.race.asian).toFixed(1) }}%</div>
              <div>Indiano:{{ parseFloat(face.race.indian).toFixed(1) }}%</div>
              <div>Negro:{{ parseFloat(face.race.black).toFixed(1) }}%</div>
              <div>Branco:{{ parseFloat(face.race.white).toFixed(1) }}%</div>
              <div class="text-bold text-red">Predominância: {{ face.dominant_race }} </div>
            </q-card-section>

          </q-card>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LayoutDefault',
  data () {
    return {
      diretorio: {},
      api: 'http://localhost:8000',
      storage: 'http://localhost:3000/',
      deepface: null,
      submitting: false,
    }
  },
  methods: {
    onSubmit () {
      this.submitting = true
      this.deepface = []
      axios.get(`${this.api}/analyze?url_image=${this.storage + this.diretorio.name}`)
        .then((response) => {
          this.deepface = response.data
        })
        .finally(() => {
          this.submitting = false
        })
    }
  },
}
</script>
