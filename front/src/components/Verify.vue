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
              <div id="imageContainer1">
                <img id="image1" class="img" :src="img1">
                <div id="highlight1"></div>
              </div>
              <div id="imageContainer2">
                <img id="image2" class="img" :src="img2">
                <div id="highlight2"></div>
              </div>
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
      diretorio1: { name: "" },
      diretorio2: { name: "" },
      img1: null,
      img2: null,
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
    convertTrueToLowerCase (text) {
      let regex = new RegExp("True", 'g');
      let replacedText = text.replace(regex, "true");

      regex = new RegExp("False", 'g');
      replacedText = replacedText.replace(regex, "false");

      return replacedText;
    },
    convertAndInsertImage (file, name) {
      const self = this
      var reader = new FileReader();
      reader.onload = function (e) {
        var dataURL = e.target.result;
        self[`img${name}`] = dataURL;
        self.setDimensionsImg(`highlight${name}`, `img${name}`)
      };
      reader.readAsDataURL(file);
    },
    setDimensionsImg (idElement, faceArea) {
      var highlight = document.getElementById(idElement);
      var highlightData = { ...this.deepface.facial_areas[faceArea] };
      
      highlight.style.left = highlightData.x + 'px';
      highlight.style.top = highlightData.y + 'px';
      highlight.style.width = highlightData.w + 'px';
      highlight.style.height = highlightData.h + 'px';
    },
    onSubmit () {
      this.submitting = true
      this.deepface = null

      const formData = new FormData();
      formData.append('image1', this.diretorio1);
      formData.append('image2', this.diretorio2);

      const headers = { 'Content-Type': 'multipart/form-data' };

      axios.post(`${this.api}/verify`, formData, { headers })
        .then((response) => {
          const stringFormat = this.convertQuotes(response.data)
          const jsonFormat = JSON.parse(this.convertTrueToLowerCase(stringFormat))
          this.deepface = jsonFormat;
          console.log('this.deepface ', this.deepface );
          this.convertAndInsertImage(this.diretorio1, "1")
          this.convertAndInsertImage(this.diretorio2, "2")
          this.submitting = false
        })
    }
  },
}
</script>

<style scoped>
.my-card {
  display: grid;
  grid-template-columns: 1fr;
}
.img {
  width: auto;
  height: auto;
}


#imageContainer1, #imageContainer2 {
  position: relative;
  display: inline-block;
}
    
#highlight1, #highlight2 {
  position: absolute;
  border: 4px solid red;
}
</style>