<template>
    <v-app>
        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
                v-if="purpose == 'work'"
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    Your use of computers at work is more consistent with which of the following descriptions?
                    <template v-slot:actions>
                        <v-icon v-if="software === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="software !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="software" column>
                        <v-radio
                                label="Daily office software usage"
                                color="orange darken-3"
                                value='2D'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="Use of software that may occupy high memory"
                                color="orange darken-3"
                                value='3D'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="A large number of program projects"
                                color="orange darken-3"
                                value='DP'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    Computers need business shapes (not abrupt on formal occasions)?
                    <template v-slot:actions>
                        <v-icon v-if="business_look === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="business_look !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="business_look" column>
                        <v-radio
                                label="Yes"
                                color="orange darken-3"
                                value='yes'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="No"
                                color="orange darken-3"
                                value='no'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel
                    v-if=" software == '2D'"
            >
                <v-expansion-panel-header disable-icon-rotate>
                    Please point out the following daily office software that may be needed:
                    <template v-slot:actions>
                        <v-icon v-if="work_software === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="work_software !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="work_software_value in work_software_values.slice(0,4)"
                            :key="work_software_value"
                            multiple
                            color="orange darken-3"
                            v-model="work_software"
                            :label="work_software_value"
                            :value="work_software_value"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel
                    v-else-if=" software == '3D'"
            >
                <v-expansion-panel-header disable-icon-rotate>
                    Please point out the following software that may require high memory:
                    <template v-slot:actions>
                        <v-icon v-if="highram_software === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="highram_software !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="highram_software_value in highram_software_values.slice(0,4)"
                            :key="highram_software_value"
                            multiple
                            color="orange darken-3"
                            v-model="highram_software"
                            :label="highram_software_value"
                            :value="highram_software_value"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel
                    v-else
            >
                <v-expansion-panel-header disable-icon-rotate>
                    please point out the following may need to be run on the computer:
                    <template v-slot:actions>
                        <v-icon v-if="deep_software === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="deep_software !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="deep_software_value in deep_software_values.slice(0,4)"
                            :key="deep_software_value"
                            multiple
                            color="orange darken-3"
                            v-model="deep_software"
                            :label="deep_software_value"
                            :value="deep_software_value"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>


            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    What aspects of the notebook computer do you value very much:
                    <template v-slot:actions>
                        <v-icon v-if="constraint === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="constraint !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="i in constraint_values.slice(0,5)"
                            :key="i.index"
                            multiple
                            color="orange darken-3"
                            v-model="constraint"
                            :label="i.index"
                            :value="i.name"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>


        <!-- 学习 -->
        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
                v-if="purpose == 'study'"
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    Your use of computers in your study?
                    <template v-slot:actions>
                        <v-icon v-if="study_purpose === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="study_purpose !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="study_purpose" column>
                        <v-radio
                                label="Browse & OFFICE"
                                color="orange darken-3"
                                value='reading'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="Software Simulation & Code Writing"
                                color="orange darken-3"
                                value='coding'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="Processing Big Data & Training Neural Networks"
                                color="orange darken-3"
                                value='deeplearning'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    What aspects of the notebook computer do you value very much:
                    <template v-slot:actions>
                        <v-icon v-if="constraint === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="constraint !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="i in constraint_values.slice(0,5)"
                            :key="i.index"
                            multiple
                            color="orange darken-3"
                            v-model="constraint"
                            :label="i.index"
                            :value="i.name"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>


        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
                v-if="purpose == 'game'"
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    Are you very interested in large stand-alone games?
                    <template v-slot:actions>
                        <v-icon v-if="game_3A === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="game_3A !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="game_3A" column>
                        <v-radio
                                label="Yes"
                                color="orange darken-3"
                                value='3A'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="No"
                                color="orange darken-3"
                                value='no'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    Usually play games attention will be more inclined to special effects?
                    <template v-slot:actions>
                        <v-icon v-if="game_effect === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="game_effect !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="game_effect" column>
                        <v-radio
                                label="Yes"
                                color="orange darken-3"
                                value='yes'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="No"
                                color="orange darken-3"
                                value='no'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    What aspects of the notebook computer do you value very much:
                    <template v-slot:actions>
                        <v-icon v-if="constraint === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="constraint !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="i in constraint_values.slice(0,5)"
                            :key="i.index"
                            multiple
                            color="orange darken-3"
                            v-model="constraint"
                            :label="i.index"
                            :value="i.name"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>


        <!--视频-->
        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
                v-if="purpose == 'video'"
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    What aspects of the notebook computer do you value very much:
                    <template v-slot:actions>
                        <v-icon v-if="constraint === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="constraint !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="i in constraint_values.slice(0,5)"
                            :key="i.index"
                            multiple
                            color="orange darken-3"
                            v-model="constraint"
                            :label="i.index"
                            :value="i.name"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>


        <!--        &lt;!&ndash;提交按钮&ndash;&gt;-->
        <div>
            <v-btn
                    rounded
                    class="ma-2"
                    color="primary"
                    dark
                    v-on:click="submit"
            >Submit
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
        name: "QuestionnaireEn_2",
        data() {
            return {
                // 第1页问题答案
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

                // 无用答案
                business_look: '',
                work_software: '',
                highram_software: '',
                deep_software: '',
                game_effect: '',

                // 问题选项
                work_software_values: ['OFFICE 3 sets', 'Small Programming Projects, Data Processing Projects', 'Two-dimensional drawing software, Graphic design software', 'Other'],
                highram_software_values: ['Use video editing software', '3D Modeling Software', 'Virtual Machine', 'Other'],
                deep_software_values: ['Major Project Projects', 'Big data operations', 'Neural Network Training', 'Other'],
                constraint_values: [
                    {index: 'Price', name: 'price'},
                    {index: 'Brand', name: 'brand'},
                    {index: 'Weight', name: 'weight'},
                    {index: 'Battery', name: 'battery_life'},
                    {index: 'Screen Size', name: 'screen_size'},
                ],

                // 功能变量
                fab: false, // 浮动按钮显示
                active_question: 0,
                degree: '',  // 控制进度条
                num_question: 3,
                num_ans: 0, //已回答问题数
            }
        },
        created() {
            this.price = this.$route.params.price;
            this.brand = this.$route.params.brand;
            this.purpose = this.$route.params.purpose;
            this.rgb_require = this.$route.params.rgb_require;
            this.bringout = this.$route.params.bringout;
            this.screen = this.$route.params.screen;

            if (this.purpose == 'work') {
                this.num_question = 3
            } else if (this.purpose == 'study') {
                this.num_question = 1
            } else if (this.purpose == 'game') {
                this.num_question = 2
            } else if (this.purpose == 'video') {
                this.num_question = 0
            }

        },
        methods: {
            submit() {
                // 跳转到下一页
                this.$router.push(
                    {
                        name: 'OutputEn',
                        params: {
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
                    });
            },

            jump() {
                // 计算完成情况
                let count_ans = 0;

                let flag = {
                    software: this.software,
                    study_purpose: this.study_purpose,
                    game_3A: this.game_3A,
                    constraint: this.constraint,
                    business_look: this.business_look,
                    work_software: this.work_software,
                    highram_software: this.highram_software,
                    deep_software: this.deep_software,
                    game_effect: this.game_effect,
                }

                for (let i = 0; i < Object.keys(flag).length; i++) {
                    if (Object.values(flag)[i] !== '') {
                        count_ans += 1
                    }
                }

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