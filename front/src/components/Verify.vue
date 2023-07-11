<template>
  <div class="q-ma-lg">
    <div class="q-pa-md">
      <div class="q-gutter-md">
        <q-form @submit="onSubmit">
          <div class="row itens-center">
            <div class="col-5 q-ma-sm">
              <label for="diretorio">Selecione foto1</label>
              <q-file required @input="() => deepface = null" filled v-model="diretorio1" label="Diretório" />
            </div>

            <div class="col-5 q-ma-sm">
              <label for="diretorio">Selecione a foto2</label>
              <q-file required @input="() => deepface = null" filled v-model="diretorio2" label="Diretório" />
            </div>
          </div>

          <q-btn :loading="submitting" color="green" class="q-ma-sm" type="submit" label="Enviar" />
        </q-form>
        <div>
          <q-card class="my-card" v-if="deepface">
            <div class="flex">
              <img class="img q-ma-md" :src="storage + diretorio1.name">
              <img class="img q-ma-md" :src="storage + diretorio2.name">
            </div>

            <div>
              <q-card-section>
                <div class="text-h6">{{ diretorio1.name }} + {{ diretorio2.name }}</div>
                <div class="text-subtitle2">Verificar fotos</div>
              </q-card-section>
              <q-card-section>
                <div class="text-h6">Aprovado?</div>
                <div class="text-bold text-red">{{ deepface.verified ? "Sim" : "Não" }}</div>
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
  name: 'PagVerify',
  data () {
    return {
      diretorio1: {name: ""},
      diretorio2: {name: ""},
      api: 'http://localhost:8000',
      storage: 'http://localhost:3000/',
      deepface: null,
      submitting: false,
    }
  },
  methods: {
    convertQuotes (str) {
      // Replace double quotes with a placeholder
      str = str.replace(/"/g, '###DOUBLE_QUOTE###');

      // Replace single quotes with double quotes
      str = str.replace(/'/g, '"');

      // Replace the placeholder with single quotes
      str = str.replace(/###DOUBLE_QUOTE###/g, "'");

      return str;
    },
    convertTrueToLowerCase(text) {
      let regex = new RegExp("True", 'g');
      let replacedText = text.replace(regex, "true");

      regex = new RegExp("False", 'g');
      replacedText = replacedText.replace(regex, "false");

      return replacedText;
    },
    onSubmit () {
      this.submitting = true
      this.deepface = null

      axios.get(`${this.api}/verify?url_image1=${this.storage + this.diretorio1.name}&url_image2=${this.storage + this.diretorio2.name}`)
        .then((response) => {
          const stringFormat = this.convertQuotes(response.data)
          const jsonFormat = JSON.parse(this.convertTrueToLowerCase(stringFormat))
          this.deepface = jsonFormat;
        })
        .finally(() => {
          this.submitting = false
        })
    }
  },
}
</script>

<style scoped>
.my-card {
  display: grid;
  grid-template-columns:  1fr;
}

.img {
  width: min-content;
  height: 19rem;
}
</style>