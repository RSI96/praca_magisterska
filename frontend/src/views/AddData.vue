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
    <div class="large-12 medium-12 small-12 cell">
      <input type="text" class="form-control" placeholder="column name" v-model="columnName">
      <button v-on:click="submitColumn()">AddColumnName</button>
    </div>
    <div>
      <select v-model="selected">
        <option v-for="option in columnList" :key="option.text">
          {{ option.text }}
        </option>
      </select>
      <span>Selected: {{ selected }}</span>
    </div>
    <div>
      <button v-on:click="submitColumn()">AddSelectedColumn</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { HTTP } from "../http-common";

export default {
  name: "addData",
  data() {
    return {
      file: '',
      columnName: null,
      selected: 'Default',
      columnList: [
        {text: 'Default'},
        {text: 'SecondOption'}
      ]
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
        try {
            const response = HTTP.post(`http://localhost:5000/parameterPrototype`, {
              'column_name': this.selected
            })
            console.log(response)
        } catch (e) {
            this.errors.push(e)
        }
    }
  },
};
</script>