<template>
    <v-app>
        <v-card
                color="grey lighten-4"
                flat
                tile
        >
            <v-toolbar>
                <v-app-bar-nav-icon></v-app-bar-nav-icon>

                <v-toolbar-title>问卷</v-toolbar-title>

                <v-spacer></v-spacer>

                <v-btn icon>
                    <v-icon>mdi-magnify</v-icon>
                </v-btn>

                <v-btn icon>
                    <v-icon>mdi-heart</v-icon>
                </v-btn>

                <v-btn icon>
                    <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
            </v-toolbar>
        </v-card>

        <v-container>
            <v-col
                    align-self="start"
                    align="left"
                    justify="center"
            >
<!--                <v-card-->
<!--                >-->
                    <p><br>您在日常生活的笔记本使用中是否只使用以下简单的软件如:OFFICE
                        三件套，编程软件，数据处理，统计软件（SPSS,MATLAB,STATA），二维制图软件（平面CAO），平面设计软件（PS，AI）等?</p>
                    <v-radio-group
                            column
                            label=""
                            messages="这里可以输入提示信息"
                            v-model="q1">
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value=true
                        ></v-radio>
                        <v-radio
                                label="不是"
                                color="orange darken-3"
                                value=false
                        ></v-radio>
                    </v-radio-group>
<!--                </v-card>-->


                <p>您是否是以下相关职业： 剪辑师、建筑师、工程师、设计师、动漫美术等？ 或经常使用三维建模软件:如LIG,3DMAS,CAO(3D),PROE,BIM,CIATA,SOLIDWORKS等，
                    或经常使用视频剪辑软件如：PR,AE,VEGAS等。
                </p>
                <v-radio-group
                        label=""
                        v-model="q2" column>
                    <v-radio
                            label="是"
                            color="orange darken-3"
                            value=true
                    ></v-radio>
                    <v-radio
                            label="不是"
                            color="orange darken-3"
                            value=false
                    ></v-radio>
                </v-radio-group>
            </v-col>
        </v-container>


        <div>
            <v-btn
                    rounded class="ma-2" color="primary" dark v-on:click="submit">Submit
                <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
            </v-btn>
        </div>


        <!--        底部组件-->
        <v-card height="">
            <v-footer
                    fixed
                    class="font-weight-medium"
            >
                <v-col
                        class="text-center"
                        cols="12"
                >
                    {{ new Date().getFullYear() }} — <strong>Chen Jiajun</strong>
                    <!--                    <v-icon>mid-heart</v-icon>-->
                </v-col>
            </v-footer>
        </v-card>

    </v-app>
</template>

<script>
    export default {
        name: "questionnaire",
        data() {
            return {
                q1: ' ',
                q2: ' ',
                q3: ' ',
                q4: ' ',
                q5: ' ',
                q6: ' ',
                q7: ' ',
                q8: ' ',
                q9: ' ',
                q10: ' ',
                q11: ' ',
                q12: ' ',
                q13: ' ',
                q14: ' ',
                output: {name: ''},
                test_function: ''
            }
        },
        methods: {
            submit() {
                // Key名存储
                let res = {
                    B_1: this.q1,
                    A_1: this.q2,
                    A_2: this.q3,
                    G_1: this.q4,
                    Apple: this.q5,
                    Budget: this.q6,
                    High_refresh: this.q7,
                    FPS: this.q8,
                    Camera: this.q9,
                    High_SSD: this.q10,
                    RGB: this.q11,
                    big_screen: this.q12,
                    Heavyable: this.q13,
                    battery_life: this.q14
                }

                // 创建传输字符串
                function create_res(res) {
                    let values = Object.values(res);
                    let res_str = '';
                    let count = 0;
                    for (let keys in res) {
                        if (res_str === '') {
                            res_str = keys + '=' + values[count];
                        } else {
                            res_str = res_str + '&' + keys + '=' + values[count];
                        }
                        count++;
                    }
                    return res_str;
                }

                let res_str = create_res(res);
                // console.log('post: ' + res_str);
                console.log('post: ' + JSON.stringify(res));

                fetch('http://127.0.0.1:5000/interface', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }, // this line is important, if this content-type is not set it wont work
                    body: res_str,
                    mode: 'cors',
                })
                    .then(response => response.json())
                    .then(response => {
                        // console.log('Success, response is:', JSON.stringify(response));
                        // console.log(typeof response);
                        for (const i in response) {
                            this.output[i] = response[i];
                        }
                        console.log('output: ' + JSON.stringify(this.output))
                    })
                    .catch(error => console.error('Error:', error));
            },
            submittest() {
                let test_res = {
                    'function': this.test_function,
                }

                // 创建可传输的字符串
                function create_res_str(res) {
                    // let keymap = Object.keys(res);
                    let values = Object.values(res);
                    let res_str = '';
                    let count = 0;
                    for (let keys in res) {
                        if (res_str === '') {
                            res_str = keys + '=' + values[count];
                        } else {
                            res_str = res_str + '&' + keys + '=' + values[count];
                        }
                        count++;
                    }
                    return res_str;
                }

                let res_str = create_res_str(test_res);

                console.log('post: ' + res_str);

                fetch('http://127.0.0.1:5000/interface', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }, // this line is important, if this content-type is not set it wont work
                    body: res_str,
                    mode: 'cors',
                })
                    .then(response => response.json())
                    .then(response => console.log('Success, response is:', JSON.stringify(response)))
                    .catch(error => console.error('Error:', error));
            }
            //         getoutput() {
            //             fetch('http://127.0.0.1:5000/interface', {
            //                 // mode: 'no-cors'
            //             })
            //                 .then(
            //                     function (response) {
            //                         if (response.status !== 200) {
            //                             console.log('Looks like there was a problem. Status Code: ' +
            //                                 response.status);
            //                             return;
            //                         }
            //
            //                         // Examine the text in the response
            //                         response.json().then(function (data) {
            //                             console.log(data);
            //                         });
            //                     }
            //                 )
            //                 .catch(function (err) {
            //                     console.log('Fetch Error :-S', err);
            //                 });
            //         },
            //         getoutput1() {
            //             console.log(JSON.stringify({num1: '2', num2: '3'}));
            //
            //             // const formData = new FormData();
            //             //
            //             // let data = {a: '1', b: '2'}
            //             // for (const name in data) {
            //             //     formData.append(name, data[name]);
            //             // }
            //             fetch('http://127.0.0.1:5000/interface', {
            //                 method: 'POST',
            //                 headers: {
            //                     'Content-Type': 'application/x-www-form-urlencoded'
            //                     // 'Content-Type': 'application/json'
            //                 }, // this line is important, if this content-type is not set it wont work
            //                 body: 'num1=2&num2=3',
            //                 mode: 'cors',
            //             })
            //                 .then(response => response.json())
            //                 .then(response => console.log('Success:', JSON.stringify(response)))
            //                 .catch(error => console.error('Error:', error));
            //         }
            //     }
        }
    }
</script>

<style scoped>
    .text-wrapper {
        white-space: pre-wrap;
    }
</style>