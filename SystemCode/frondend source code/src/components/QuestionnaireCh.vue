<template>
    <v-app>
        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你购买电脑的预算最接近以下哪个数字？
                    <template v-slot:actions>
                        <!--                        <v-icon v-if="is_finish[0] === 0" color="error">mdi-alert-circle</v-icon>-->
                        <v-icon v-if="price === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="price !== ''" color="teal">mdi-check</v-icon>
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="price" column>
                        <v-radio
                                label="¥ 4000"
                                color="orange darken-3"
                                value='4000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 5000"
                                color="orange darken-3"
                                value='5000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 6000"
                                color="orange darken-3"
                                value='6000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 7000"
                                color="orange darken-3"
                                value='7000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 8000"
                                color="orange darken-3"
                                value='8000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 9000"
                                color="orange darken-3"
                                value='9000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 10000"
                                color="orange darken-3"
                                value='10000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ >10000"
                                color="orange darken-3"
                                value='11000'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你是否只想要苹果电脑（MacBook）？
                    <template v-slot:actions>
                        <v-icon v-if="brand.length === 0" color="primary">$expand</v-icon>
                        <v-icon v-else-if="brand.length !== 0" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="brand" column>
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value='apple'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="不是"
                                color="orange darken-3"
                                value='none'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你选购的电脑主要出于以下什么用途？
                    <template v-slot:actions>
                        <v-icon v-if="purpose === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="purpose !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="purpose" column>
                        <v-radio
                                label="看视频或者浏览网页，娱乐用途"
                                color="orange darken-3"
                                value='video'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="工作"
                                color="orange darken-3"
                                value='work'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="学习"
                                color="orange darken-3"
                                value='study'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="玩游戏，并且对游戏画质有较高的要求"
                                color="orange darken-3"
                                value='game'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>


            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    你希望有酷炫的彩色RGB灯带键盘吗？（RGB灯带可开可关）
                    <template v-slot:actions>
                        <v-icon v-if="rgb_require === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="rgb_require !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="rgb_require" column>
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value='true'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="不是"
                                color="orange darken-3"
                                value='false'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问您是否经常会携带你的电脑外出或者希望电脑具备较强的续航能力？
                    <template v-slot:actions>
                        <v-icon v-if="bringout === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="bringout !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="bringout" column>
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value='yes'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="不是"
                                color="orange darken-3"
                                value='no'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>


            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你对屏幕大小和重量更满足以下哪一类？
                    <template v-slot:actions>
                        <v-icon v-if="screen === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="screen !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="screen" column>
                        <v-radio
                                label="屏幕要大，重不重无所谓"
                                color="orange darken-3"
                                value='big'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="中等，15.6寸就很标准"
                                color="orange darken-3"
                                value='medium'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="小一些，我喜欢小巧轻便的"
                                color="orange darken-3"
                                value='small'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="无所谓"
                                color="orange darken-3"
                                value='dontcare'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>


            <!--Q8 多选-->
            <v-expansion-panel v-if="flag_addq2 == true">
                <v-expansion-panel-header disable-icon-rotate>
                    以下是2020年对笔记本品牌效应的评估，请选择一个你非常喜欢的品牌。
                    <template v-slot:actions>
                        <v-icon v-if="brand === 'none'" color="primary">$expand</v-icon>
                        <v-icon v-else-if="brand !== 'none'" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content class="text-left">
                    一线品牌<br>
                    具有对笔记本模具的设计能力和拥有自己的代工厂，售后网点全国铺开。
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="i in first_brands.slice(0,4)"
                                        :key="i.index"
                                        multiple
                                        color="orange darken-3"
                                        v-model="brand"
                                        :label="i.index"
                                        :value="i.name"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="i in first_brands.slice(4,8)"
                                        :key="i.index"
                                        multiple
                                        color="orange darken-3"
                                        v-model="brand"
                                        :label="i.index"
                                        :value="i.name"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="i in first_brands.slice(8,12)"
                                        :key="i.index"
                                        multiple
                                        color="orange darken-3"
                                        v-model="brand"
                                        :label="i.index"
                                        :value="i.name"
                                >
                                </v-checkbox>
                            </v-col>
                        </v-row>
                    </v-container>

                    二线品牌<br>
                    贴牌其他厂家的产品进行销售。
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="i in second_brands.slice(0,3)"
                                        :key="i.index"
                                        multiple
                                        color="orange darken-3"
                                        v-model="brand"
                                        :label="i.index"
                                        :value="i.name"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="i in second_brands.slice(3,6)"
                                        :key="i.index"
                                        multiple
                                        color="orange darken-3"
                                        v-model="brand"
                                        :label="i.index"
                                        :value="i.name"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="i in second_brands.slice(6,9)"
                                        :key="i.index"
                                        multiple
                                        color="orange darken-3"
                                        v-model="brand"
                                        :label="i.index"
                                        :value="i.name"
                                >
                                </v-checkbox>
                            </v-col>
                        </v-row>
                    </v-container>

                    三线品牌<br>
                    以较低的价格提供较高的配置。
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="i in third_brands.slice(0,1)"
                                        :key="i.index"
                                        multiple
                                        color="orange darken-3"
                                        v-model="brand"
                                        :label="i.index"
                                        :value="i.name"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="i in third_brands.slice(1,2)"
                                        :key="i.index"
                                        multiple
                                        color="orange darken-3"
                                        v-model="brand"
                                        :label="i.index"
                                        :value="i.name"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="i in third_brands.slice(2,3)"
                                        :key="i.index"
                                        multiple
                                        color="orange darken-3"
                                        v-model="brand"
                                        :label="i.index"
                                        :value="i.name"
                                >
                                </v-checkbox>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>


        <!--提交按钮-->
        <div>
            <v-btn
                    rounded
                    class="ma-2"
                    color="primary"
                    dark
                    v-on:click="submit"
            >下一页
                <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
            </v-btn>
        </div>


        <!--进度条组件-->
        <v-progress-linear
                fixed
                background-opacity="0.3"
                :value="degree"
                color="primary"
        ></v-progress-linear>


        <!--浮动按钮-->
        <v-speed-dial
                v-model="fab"
                fixed
                bottom
                left
                direction="top"
                transition="slide-y-reverse-transition"

        >
            <template v-slot:activator>
                <v-btn
                        v-model="fab"
                        color="blue darken-2"
                        dark
                        fab
                >
                    <v-icon v-if="fab">mdi-close</v-icon>
                    <v-icon v-else>mdi-menu</v-icon>
                </v-btn>
            </template>
            <v-btn
                    fab
                    dark
                    small
                    color="green"
            >
                En/Ch
            </v-btn>
            <v-btn
                    fab
                    dark
                    small
                    color="indigo"
            >
                <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-btn
                    fab
                    dark
                    small
                    color="red"
            >
                <v-icon>mdi-account-circle</v-icon>
            </v-btn>
        </v-speed-dial>


    </v-app>

</template>

<script>
    export default {
        name: "QuestionnaireCh",
        data() {
            return {
                // 第一页问题的答案
                price: '',
                brand: [],
                purpose: '',
                rgb_require: '',
                bringout: '',
                screen: '',

                // 品牌硬编码
                first_brands: [
                    {index: '联想', name: 'Lenovo'},
                    {index: '华硕', name: 'ASUS'},
                    {index: '微星', name: 'msi'},
                    {index: '技嘉', name: 'GIGABYTE'},
                    {index: '戴尔', name: 'DELL'},
                    {index: '惠普', name: 'hp'},
                    {index: 'ThinkPad', name: 'ThinkPad'},
                    {index: '华为', name: 'HUAWEI'},
                    {index: '宏碁', name: 'Acer'},
                    {index: 'ROG', name: 'ROG'},
                    {index: '外星人', name: 'Alienware'},
                    {index: '微软', name: 'microsoft'},
                ],
                second_brands: [
                    {index: '三星', name: 'samsung'},
                    {index: '神州', name: 'Hasee'},
                    {index: '机械革命', name: 'MECHREVO'},
                    {index: '雷蛇', name: 'Razer'},
                    {index: '红米', name: 'Redmi'},
                    {index: '雷神', name: 'Thunderobot'},
                    {index: '荣耀', name: 'Honor'},
                    {index: '小米', name: 'xiaomi'},
                    {index: '炫龙', name: 'xuanlong'},
                ],
                third_brands: [
                    {index: 'A豆', name: 'adou'},
                    {index: '机械师', name: 'MACHENIKE'},
                    {index: '火影', name: 'huoying'}
                ],

                // 功能变量
                fab: false, // 浮动按钮显示
                active_question: 0, // 激活题目的索引，从0开始
                degree: '',  // 控制进度条
                num_question: 6, // 总问题数
                num_ans: 0, //已回答问题数
                flag_addq2: false, //q2增加问题标志
            }
        },

        methods: {
            submit() {
                // Key名存储
                // let res = {
                //     price: this.price,
                //     purpose: this.purpose,
                //     brand: this.brand,
                //     // use_time: this.use_time,
                //     game: this.game,
                //     game_3A: this.game_3A,
                //     software: this.software,
                //     study_purpose: this.study_purpose,
                //     bringout: this.bringout,
                //     screen: this.screen,
                // }
                //
                // // 创建传输字符串
                // function create_res(res) {
                //     let values = Object.values(res);
                //     let res_str = '';
                //     let count = 0;
                //     for (let keys in res) {
                //         if (res_str === '') {
                //             res_str = keys + '=' + values[count];
                //         } else {
                //             res_str = res_str + '&' + keys + '=' + values[count];
                //         }
                //         count++;
                //     }
                //     return res_str;
                // }
                //
                // let res_str = create_res(res);
                // // console.log('post: ' + res_str);
                // // console.log('post: ' + JSON.stringify(res));
                //
                // fetch('http://127.0.0.1:5000/interface', {
                //     method: 'POST',
                //     headers: {
                //         'Content-Type': 'application/x-www-form-urlencoded'
                //     }, // this line is important, if this content-type is not set it wont work
                //     body: res_str,
                // })
                //     .then(response => response.json())
                //     .then(response => {
                //         // for (let i = 0; i < Object.keys(response).length; i++)
                //         //     console.log('output: ' + JSON.stringify(response[i]));
                //
                //         this.output = response;
                //         console.log('output ' + JSON.stringify(this.output));
                //         console.log('output type' + typeof output);
                //     })
                // 跳转到下一页
                this.$router.push(
                    {
                        name: 'QuestionnaireCh_2',
                        params: {
                            price: this.price,
                            purpose: this.purpose,
                            brand: this.brand,
                            rgb_require: this.rgb_require,
                            bringout: this.bringout,
                            screen: this.screen,
                        }
                    });
            },

            jump() {
                // 计算完成情况
                let count_ans = 0;
                let flag = {
                    price: this.price,
                    purpose: this.purpose,
                    rgb_require: this.rgb_require,
                    brand: this.brand,
                    bringout: this.bringout,
                    screen: this.screen,
                }
                // 更改问题总数
                // q2
                if (this.brand === 'none' && this.flag_addq2 == false) {
                    // this.num_question += 1;
                    this.flag_addq2 = true;
                } else if (this.brand === 'apple' && this.flag_addq2 == true) {
                    // this.num_question -= 1;
                    this.flag_addq2 = false;
                }

                for (let i = 0; i < Object.keys(flag).length; i++) {
                    if (Object.values(flag)[i] !== '') {
                        count_ans += 1
                    }
                }

                // 测试输出
                // console.log('now question is ' + length(this.active_question))
                // console.log('active question just now: ' + this.active_question)
                // console.log('active question now: ' + this.active_question)

                // 跳转到下一个问题
                this.active_question += 1

                // 控制进度条
                this.degree = count_ans / this.num_question * 100

            },
        }
    }
</script>

<style scoped>

</style>