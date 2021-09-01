<template>
  <div class="page">
    <h2>Add .csv files here</h2>
    <div class="large-12 medium-12 small-12 cell">
      <label
        >File
        <input
          type="file"
          id="file"
          ref="file"
          v-on:change="handleFileUpload()"
        />
      </label>
      <button v-on:click="submitFile()">Submit</button>
    </div>
    <div>
      <select v-model="selectedColumnName">
        <option v-for="option in columnList" :key="option.text">
          {{ option.text }}
        </option>
      </select>
      <span>Selected: {{ selectedColumnName }}</span>
    </div>
    <div>
      <button v-on:click="submitColumn()">AddSelectedColumn</button>
      <br>
      <span>Result: {{ result }}</span>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "addData",
  data() {
    return {
      file: '',
      columnName: null,
      selectedColumnName: 'Default',
      fileName: 'Default',
      columnList: [
        {text: 'Default'},
        {text: 'SecondOption'}
      ],
      result: []
    };
  },
  methods: {
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);

      axios
        .post("http://localhost:5000/addFile", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(response => (this.columnList = response.data))
        .then(response => (console.log(response.data)))
        .catch(error => console.log(error))
        ;
    },
    submitColumn() {
      axios
        .post("http://localhost:5000/addSelectedColumnName", {
              column_name: this.selectedColumnName,
              dataset_name: this.file.name
            })
        .then(response => (this.result = response.data))
        .then(response => (console.log(response.data)))
        .catch(error => console.log(error))
        ;
    }
  },
};
</script>