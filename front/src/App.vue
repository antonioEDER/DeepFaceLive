<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md">
      <q-card>
        <q-tabs
          v-model="tab"
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="analyse" label="Analisar"/>
          <q-tab name="verify" label="Verificar" />
        </q-tabs>

        <q-separator />

        <q-tab-panels v-model="tab" animated>
          
          <q-tab-panel name="analyse">
            <Analyze />
          </q-tab-panel>

          <q-tab-panel name="verify">
            <Verify />
          </q-tab-panel>

        </q-tab-panels>
      </q-card>
    </div>
  </div>
</template>

<script>
import Analyze from './components/Analyze.vue';
import Verify from './components/Verify.vue';

export default {
  name: 'App',
  data () {
    return {
      tab: 'analyse'
    }
  },
  components: {
    Analyze,
    Verify
  }
}
</script>
