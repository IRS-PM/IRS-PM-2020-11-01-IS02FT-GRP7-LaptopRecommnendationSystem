<template>
    <v-app>
        <div>
            <v-container fluid>
                <v-row>
                    <v-col cols="12">
                        <v-row
                                class="grey lighten-5"
                                style="height: 280px;"
                        >
                            <v-card
                                    v-for="output_id in [0,1,2]"
                                    :key="output_id"
                                    class="mx-auto"
                                    max-width="300"
                                    elevation="5"
                            >
                                <v-img
                                        class=""
                                        height="200px"
                                        :src="output[output_id]['img_src']"
                                >

                                </v-img>

                                <v-card-title>{{ output[output_id]['name'] }}</v-card-title>

                                <v-card-subtitle
                                        class="v-card__title"

                                >￥ {{ output[output_id]['price'] }}
                                </v-card-subtitle>

                                <v-card-subtitle class="pb-0">配置一览</v-card-subtitle>

                                <v-card-text class="text--primary">
                                    <v-simple-table>
                                        <template v-slot:default>
                                            <tbody>
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >CPU
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['cpu'] }}</td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >GPU
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['gpu'] }}</td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >内存
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['ram'] }}GB</td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >硬盘
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['disk'] }}</td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >重量
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['weight'] }}</td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >屏幕尺寸
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['screen_size'] }}</td>
                                            </tr>
                                            </tbody>
                                        </template>
                                    </v-simple-table>
                                </v-card-text>

                                <v-card-subtitle class="pb-0">特性</v-card-subtitle>
                                <v-card-text>
<!--                                    <v-chip-->
<!--                                            v-if="output[output_id]['is_rtx'] != 0"-->
<!--                                            text-color="white"-->
<!--                                            rounded-->
<!--                                            color="orange"-->
<!--                                    >-->
<!--                                        <v-icon left>mdi-star</v-icon>-->
<!--                                        适合深度学习-->
<!--                                    </v-chip>-->
                                    <v-chip
                                            v-if="output[output_id]['cpu_rank'] == 9"
                                            text-color="white"
                                            rounded
                                            color="orange"
                                    >
                                        <v-icon left>mdi-star</v-icon>
                                        高性能CPU
                                    </v-chip>
                                    <v-chip
                                            v-if="output[output_id]['ram'] >= 16"
                                            text-color="white"
                                            rounded
                                            color="orange"
                                    >
                                        <v-icon left>mdi-star</v-icon>
                                        大容量RAM
                                    </v-chip>
                                    <v-chip
                                            v-if="output[output_id]['weight_type'] == 'light'"
                                            text-color="white"
                                            rounded
                                            color="orange"
                                    >
                                        <v-avatar left>
                                            <v-icon>mdi-star</v-icon>
                                        </v-avatar>
                                        便携
                                    </v-chip>
                                    <v-chip
                                            v-if="output[output_id]['battery_life'] == 'long'"
                                            text-color="white"
                                            rounded
                                            color="orange"
                                    >
                                        <v-avatar left>
                                            <v-icon>mdi-star</v-icon>
                                        </v-avatar>
                                        续航强劲
                                    </v-chip>

                                    <v-chip
                                            v-if="output[output_id]['has_camere'] == 'TRUE'"
                                            text-color="white"
                                            rounded
                                            color="primary"
                                    >
                                        <v-avatar left>
                                            <v-icon>mdi-checkbox-marked-circle</v-icon>
                                        </v-avatar>
                                        有摄像头
                                    </v-chip>
                                    <v-chip
                                            v-if="output[output_id]['screen_size'] == '17.3'"
                                            text-color="white"
                                            rounded
                                            color="primary"
                                    >
                                        <v-avatar left>
                                            <v-icon>mdi-checkbox-marked-circle</v-icon>
                                        </v-avatar>
                                        大屏幕
                                    </v-chip>

                                    <v-chip
                                            v-else-if="output[output_id]['has_camere'] == 'FALSE'"
                                            text-color="white"
                                            rounded
                                            color="red"
                                    >
                                        <v-avatar left>
                                            <v-icon>mdi-cancel</v-icon>
                                        </v-avatar>
                                        无摄像头
                                    </v-chip>

                                </v-card-text>

                                <v-card-actions>
                                    <v-btn
                                            color="orange"
                                            text
                                            :href="output[output_id]['link']"
                                    >
                                        ZOL
                                    </v-btn>
                                    <v-btn
                                            color="orange"
                                            text
                                            href="https://search.jd.com/Search?keyword=%E5%A4%96%E8%AE%BE&enc=utf-8&wq=%E5%A4%96%E8%AE%BE&pvid=0a882df14ac6457ba4077b01b7cd7926"
                                    >
                                        外设购买
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-row>
                    </v-col>
                </v-row>
            </v-container>
        </div>


        <v-speed-dial
                fixed
                bottom
                left
                direction="top"
                transition="slide-y-reverse-transition"

        >
            <template v-slot:activator>
                <v-btn
                        color="blue darken-2"
                        dark
                        fab
                        v-on:click="back"
                >
                    <v-icon>mdi-arrow-left-circle</v-icon>
                </v-btn>
            </template>
        </v-speed-dial>

    </v-app>
</template>

<script>
    export default {
        pat: '/output',
        data() {
            return {
                price: '',
                brand: [],
                purpose: '',
                rgb_require: '',
                bringout: '',
                screen: '',

                // 第2页问题答案
                software: '',
                study_purpose: '',
                game_3A: '',
                constraint: '',

                // 输出结果
                output: {},

                // 解释器参数
                fit1: false,
            }
        },
        created() {
            this.price = this.$route.params.price;
            this.purpose = this.$route.params.purpose;
            this.brand = this.$route.params.brand;
            this.rgb_require = this.$route.params.rgb_require;
            this.bringout = this.$route.params.bringout;
            this.screen = this.$route.params.screen;
            this.game_3A = this.$route.params.game_3A;
            this.software = this.$route.params.software;
            this.study_purpose = this.$route.params.study_purpose;
            this.constraint = this.$route.params.constraint;

            let res = {
                price: this.price,
                purpose: this.purpose,
                brand: this.brand,
                rgb_require: this.rgb_require,
                bringout: this.bringout,
                screen: this.screen,
                software: this.software,
                study_purpose: this.study_purpose,
                game_3A: this.game_3A,
                constraint: this.constraint,
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
            console.log('post: ' + JSON.stringify(res));

            fetch('http://127.0.0.1:5000/interface', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }, // this line is important, if this content-type is not set it wont work
                body: res_str,
            })
                .then(response => response.json())
                .then(response => {
                    console.log('post: ' + JSON.stringify(res));
                    for (let i = 0; i < Object.keys(response).length; i++)
                        console.log('output: ' + JSON.stringify(response[i]));

                    this.output = response;

                    if(Object.keys(this.output[0])[0] == 'mes')
                    {
                        alert("无法推理结果，请重新填写问卷再试")
                        this.$router.go(-2);
                    }
                    //console.log('output type ' + typeof JSON.stringify(this.output));
                })

            // function tranlate_res(output) {
            //     if (output['is_rtx'] !== '0')
            //         this.fit1 = true
            // }
            //
            // tranlate_res(this.output[0])
        },
        methods: {
            back() {
                /* 返回第一页回答 */
                this.$router.go(-2);
            }
        }

    }
</script>

<style scoped>

</style>